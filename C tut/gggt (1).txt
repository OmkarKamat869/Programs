
#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>
#include <windows.h>

struct person
{
    char name[35];
    char mble_no[11];
};

void menu();
void got();
void start();
void back();
void add();
void list();
void alter();
void deleter();
void search();

int main()
{
    start();
    return 0;
}
void back()
{
    start();
}
void start()
{
    menu();
}
void menu()
{
    printf("\t\t\t\t    ********** PHONEBOOK**********");

    printf("\n\n\t\t\t\t\t\t MENU\t\t\n\n");
    printf("\t1.Add\t  2.List\t  3.Alter\t  4.Look\t  5.Delete\t  6.Exit\n\n");

    switch (getch())
    {
        case '1':
            add();
            break;
        case '2':
            list();
            break;
        case '3':
            alter();
            break;
        case '4':
            search();
            break;
        case '5':
            deleter();
            break;
        case '6':
            exit(0);
            break;
        
        default:
            printf("\n\t\tEnter 1 to 6 only\n");
            printf("\n \t\tEnter any key\n");
            getch();
            menu();
    }
}
void add()
{
    FILE *f;
    struct person p;
    char nm1[100],p1[12];
    int a;
    f = fopen("project", "ab+");
    
    printf("\n Enter name: ");
    got(nm1);
    printf("\nEnter phone no.:");
    scanf("%s",p1);
    a=strlen(p1);
    if(a!=10){
        printf("\t\t!!Invalid phone number!!\n");
        printf("\t\tEnter a ten digit phone number\n");
        exit(0);
    }
    else{
    strcpy(p.name,nm1);
    strcpy(p.mble_no,p1);
    //got(p.name);
//    scanf("%s", &p.mble_no);
    fwrite(&p, sizeof(p), 1, f);
    fflush(stdin);
    printf("\nrecord saved");
    fclose(f);
    printf("\n\nEnter any key");
    getch();
    menu();
    }
}
void list()
{
    struct person p;
    FILE *f;
    f = fopen("project", "rb");
    if (f == NULL)
    {
        printf("\nContact list is empty\n");

        exit(1);
    }
    printf("\n\n\t **** MY CONTACTS ****\n\n ");
    while (fread(&p, sizeof(p), 1, f) == 1)
    {
        printf("\nName=%s\nMobile no=%s\n", p.name,  p.mble_no);

        //getch();
    }
    fclose(f);
    printf("\n\t Enter any key");
    getch();
    menu();
}
void search()
{
    struct person p;
    FILE *f;
    char name[100];

    f = fopen("project", "rb");
    if (f == NULL)
    {
        printf("\n error in opening\a\a\a\a");
        exit(1);
    }
    printf("\nEnter name of person to search\n");
    got(name);
    while (fread(&p, sizeof(p), 1, f) == 1)
    {
        if (strcmp(p.name, name) == 0)
        {
            printf("\n\nDetail Information About %s...", name);
            printf("\n\nName:%s\nMobile no:%s\n", p.name,  p.mble_no);
        }
        else
            printf("");
    }
    fclose(f);
    printf("\n Enter any key");

    getch();
    menu();
}
void deleter()
{
    struct person p;
    FILE *f, *ft;
    int flag;
    char name[100];
    f = fopen("project", "rb");
    if (f == NULL)
    {

        printf("\nCONTACT'S DATA NOT ADDED YET.\n");
    }
    else
    {
        ft = fopen("temp", "wb+");
        if (ft == NULL)

            printf("\nfile opaning error\n");
        else

        {

            printf("\nEnter CONTACT'S NAME : \n");
            got(name);

            fflush(stdin);
            while (fread(&p, sizeof(p), 1, f) == 1)
            {
                if (strcmp(p.name, name) != 0)
                    fwrite(&p, sizeof(p), 1, ft);
                if (strcmp(p.name, name) == 0)
                    flag = 1;
            }
            fclose(f);
            fclose(ft);
            if (flag != 1)
            {
                printf("\nNO CONTACT'S RECORD TO DELETE.\n");
                remove("temp.txt");
            }
            else
            {
                remove("project");
                rename("temp.txt", "project");
                printf("\nRECORD DELETED SUCCESSFULLY\n");
            }
        }
    }
    printf("\n Enter any key");

    getch();
    menu();
}

void alter()
{
    int c;
    FILE *f;
    int flag = 0;
    struct person p, s;
    char name[50];
    f = fopen("project", "rb+");
    if (f == NULL)
    {

        printf("CONTACT NOT FOUND.");
        exit(1);
    }
    else
    {
        printf("\nEnter CONTACT'S NAME TO MODIFY:\n");
        got(name);
        while (fread(&p, sizeof(p), 1, f) == 1)
        {
            if (strcmp(name, p.name) == 0)
            {

                printf("\n Enter name:");
                got(s.name);
                
                printf("\nEnter phone no:");
                scanf("%s", &s.mble_no);
               
                fseek(f, sizeof(p), SEEK_CUR);
                fwrite(&s, sizeof(p), 1, f);
                flag = 1;
                break;
            }
            fflush(stdin);
        }
        if (flag == 1)
        {
            printf("\n your data is modified");
        }
        else
        {
            printf(" \n data is not found");
        }
        fclose(f);
    }
    printf("\n Enter any key");
    getch();
    menu();
}
void got(char *name)
{

    int i = 0, j;
    char c, ch;
    do
    {
        c = getch();
        if (c != 8 && c != 13)
        {
            *(name + i) = c;
            putch(c);
            i++;
        }
        if (c == 8)
        {
            if (i > 0)
            {
                i--;
            }
            for (j = 0; j < i; j++)
            {
                ch = *(name + j);
                putch(ch);
            }
        }
    } while (c != 13);
    *(name + i) = '\0';    
}
