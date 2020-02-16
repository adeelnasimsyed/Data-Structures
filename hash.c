#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 1000

//struct to hold key, value pairs and next entry(for collisions, like linkedlist)
typedef struct entry_t
{
	char *key;
	char *value;
	struct entry_t *next;

	
}entry_t;


//hash table to hold all the entries
typedef struct  
{

	entry_t **entries;

} hashTable;

//hashing function
unsigned int hash(const char *key){

	int len = strlen(key);
	unsigned int value = 0;
	int i = 0;

	for (i; i < len; ++i)
	{
		value = value * 37 + key[i];	
	}

	value = value % TABLE_SIZE;

	return value;
}

//create hashtable
hashTable * hT_create(void){

	int i = 0;

	//allocate table
	hashTable *hT = malloc(sizeof(hashTable) * 1);
	
	//allocate table entries
	hT -> entries = malloc(sizeof(entry_t*) * TABLE_SIZE);

	//set each entry to NULL
	for (i; i < TABLE_SIZE; ++i)
	{
		hT->entries[i] = NULL;
	}

	return hT;


}

//helper function to add key value pair
entry_t *hT_pair(const char *key, const char* value){

	entry_t *newEntry = malloc(sizeof(entry_t) * 1);
	newEntry->key = malloc(strlen(key) + 1);
	newEntry->value = malloc(strlen(value) + 1);

	strcpy(newEntry->key, key);
	strcpy(newEntry->value, value);

	newEntry->next = NULL;

}

//add key value pair
void hT_add(hashTable *hT, const char *key, const char *value){

	unsigned int slot = hash(key);

	entry_t *entry = hT -> entries[slot];
	entry_t *prev;

	//if entry is NULL add new key,value pair
	if (entry == NULL){

		hT ->entries[slot] = hT_pair(key,value);
	}

	//else walk through the entries
	else{

		//go through all entries in the slot
		while(entry != NULL){

			//if match is found with the key then update value
			if (strcmp(entry->key, key) == 0){

				free(entry->value);
				entry->value = malloc(strlen(value) + 1);
				strcpy(entry->value, value);
				return;
			}

			prev = entry;
			entry = prev->next;
		}

		prev->next = hT_pair(key,value);

	}

}

//delete key value pair
void hT_del(hashTable *hT, const char *key){

	unsigned int slot = hash(key);

	entry_t *entry = hT -> entries[slot];
	entry_t *prev;
	int index = 0;

	//if entry is NULL, return
	if (entry == NULL){

		printf("The key %s does not exist in the hash map\n", key);
		return;	
	}

	else{

		//go through all entries in the slot
		while(entry != NULL){

			//if match is found with the key
			if (strcmp(entry->key, key) == 0){

				//if entry is first entry and there is no other entries
				if (entry->next == NULL && index == 0){

					hT->entries[slot] = NULL;
				}

				//if entry is first entry and there are other entries
				else if (entry->next != NULL && index == 0){

					entry = entry->next;
				}

				//if entry is last item
				else if(entry->next == NULL && index != 0){

					prev->next = NULL;

				}

				//if entry is middle item
				else if(entry->next != NULL && index != 0){

					prev->next = entry->next;
				}

				free(entry->key);
				free(entry->value);
				free(entry);

				return;

			}

			prev = entry;
			entry = entry->next;
			++index;
		}

	}

	printf("The key %s does not exist in the hash map\n", key);
	return;

}




// get value for the key
char *hT_get(hashTable *hT, const char *key){


	unsigned int slot = hash(key);

	entry_t *entry = hT -> entries[slot];

	//if entry is NULL, return
	if (entry == NULL){

		printf("The key %s does not exist in the hash map\n", key);
		return NULL;
	}

	else{

		//go through all entries in the slot
		while(entry != NULL){

			//if match is found with the key then update value
			if (strcmp(entry->key, key) == 0){

				return entry->value;
			}

			entry = entry->next;
		}

	}

	printf("The key %s does not exist in the hash map\n", key);
	return NULL;

}

// print all key value pairs in the hashtable
void hT_dump(hashTable *hT){

	int i;


	for (i = 0; i < TABLE_SIZE; ++i)
	{

		entry_t *entry = hT->entries[i];

		if(entry != NULL){

			for(;;){

				printf("key: %s   value: %s", entry->key, entry->value);

				if(entry->next == NULL){
					break;
				}

				entry = entry->next;
			}

			printf("\n");
		}

		
	}
}


void main(){

	hashTable *hash_table = hT_create();
	hT_add(hash_table, "hello", "world");
	hT_add(hash_table, "check", "test");
	hT_add(hash_table, "adeel", "syed");
	printf("%s\n", hT_get(hash_table, "adeel"));
	hT_del(hash_table, "check");
	hT_dump(hash_table);


}