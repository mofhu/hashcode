#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>

#define BOOL int
#define TRUE 1
#define FALSE 0

int logFlag = 0;

typedef struct PHOTO 
{
    int orient;
    int tagNum;
    int useNum;
    char tags[100][11];
}PHOTO;

typedef struct SLIDE
{
    int photoNum;
    int tagNum;
    int photos[2];
    char tags[200][11];
}SLIDE;

int getInt(const char *buf)
{
   const char *loc = buf;
   int res = 0;
   atoi(buf);
   loc = strstr(buf," ");
   while(loc != NULL)
   {
       atoi(loc+1);
       res++;
       loc = strstr(loc+1, " ");
   }
   return res;
}

void getSlidePhoto(char *buf, SLIDE *slide)
{
   char *loc = buf;
   slide->photos[0] = atoi(buf);
   slide->photos[1] = -1;
   slide->photoNum = 1;
   loc = strstr(buf," ");
   if (loc != NULL)
   {
       slide->photos[1] = atoi(loc+1);
       slide->photoNum = 2;
   }

   return;
}

BOOL isSameTag(SLIDE *slide, char *tag)
{
    for (int i = 0; i < slide->tagNum; i++)
    {
        if (0 == strcmp(slide->tags[i], tag))
        {
            return TRUE;
        }
    }
    return FALSE;
}

void getSlideTag(SLIDE *slide, PHOTO *photo1, PHOTO *photo2)
{
    for (int i = 0; i < photo1->tagNum; i++)
    {
        strcpy(slide->tags[i], photo1->tags[i]);
        slide->tagNum++;
    }

    if (NULL == photo2)
    {
        return;
    }

    for (int i = 0; i < photo2->tagNum; i++)
    {
        if (FALSE == isSameTag(slide, photo2->tags[i]))
        {
            strcpy(slide->tags[slide->tagNum], photo2->tags[i]);
            slide->tagNum++;
        }
    }

    return;
}

int getScore(SLIDE *slide, int slideNum)
{
    int idx     = 0;
    int score   = 0;
    int sum     = 0;
    int inBothNum   = 0;
    int inOnlyS1Num = 0;
    int inOnlyS2Num = 0;
    SLIDE *s1   = NULL;
    SLIDE *s2   = NULL;

    if (0 == slideNum)
    {
        return 0;
    }

    while (idx < slideNum-1)
    {
        s1 = &(slide[idx]);
        s2 = &(slide[idx+1]);
        inBothNum   = 0;
        inOnlyS1Num = 0;
        inOnlyS2Num = 0;

        for (int i = 0; i < s1->tagNum; i++)
        {
            if (TRUE == isSameTag(s2, s1->tags[i]))
            {
                inBothNum++;
            }
            else
            {
                inOnlyS1Num++;
            }
        }
        inOnlyS2Num = s2->tagNum - inBothNum;

        score = (inOnlyS1Num<inOnlyS2Num)?inOnlyS1Num:inOnlyS2Num;
        score = (inBothNum<score)?inBothNum:score;
        sum += score;

        if (0 != logFlag)
            printf("s%d s%d: inBoth %d, inS1:%d, inS2:%d, score:%d\n",\
                idx, idx+1, inBothNum, inOnlyS1Num, inOnlyS2Num, score);
        idx++;
    }

    return sum;
}

void printPhotos(PHOTO *photos, int num)
{
    printf("=== photos ===\n");

    for (int i = 0; i < num; i++)
    {
        printf("%d,%d,%d", i, photos[i].orient, photos[i].tagNum);
        for(int j = 0; j < photos[i].tagNum; j++)
        {
            printf(",%s", photos[i].tags[j]);
        }
        printf("\n");
    }

    printf("=== photos end ===\n\n");
    return;
}

void printSlide(SLIDE *slides, int num)
{
    printf("=== slides ===\n");

    for (int i = 0; i < num; i++)
    {
        printf("%d,%d,%d", i, slides[i].photos[0], slides[i].photos[1]);
        for(int j = 0; j < slides[i].tagNum; j++)
        {
            printf(",%s", slides[i].tags[j]);
        }
        printf("\n");
    }

    printf("=== slides end ===\n\n");
    return;
}

int main(int argc, char *argv[])
{
    FILE *fin   = NULL;
    FILE *fsub  = NULL;

    int photoNum    = 0;
    int photoIdx    = 0;

    int slideNum    = 0;
    int slideIdx    = 0;

    int score       = 0;

    int tmp = 0;
    char ch = '\0';
    char buf[20];

    PHOTO *photos = (PHOTO *)malloc(sizeof(PHOTO)*100000);
    SLIDE *slides = (SLIDE *)malloc(sizeof(SLIDE)*100000);

    memset(photos, 0, sizeof(PHOTO) * 100000);
    memset(slides, 0, sizeof(SLIDE) * 100000);

    fin     = fopen(argv[1], "r");
    fsub    = fopen(argv[2], "r");
    logFlag = atoi(argv[3]);

    printf("%s: ", argv[1]);

    fscanf(fin, "%d", &photoNum);

    if (0 != logFlag)
        printf("Photo Num: %d\n", photoNum);

    while(photoIdx < photoNum)
    {
        fgets(buf, 20, fin);    //换行

        ch = fgetc(fin);
        if ('V' == ch)
        {
            photos[photoIdx].orient = 1;
        }

        fscanf(fin, "%d", &(photos[photoIdx].tagNum));

        for (int i = 0; i < photos[photoIdx].tagNum; i++)
        {
            memset(photos[photoIdx].tags[i], 0, sizeof(char)*11);
            fscanf(fin, "%s", photos[photoIdx].tags[i]);
        }

        photoIdx++;
    }

    if (0 != logFlag)
        printPhotos(photos, photoNum);

    fscanf(fsub, "%d", &slideNum);
    if (0 != logFlag)
        printf("Slide Num: %d\n", slideNum);

    fgets(buf, 20, fsub);

    while(slideIdx < slideNum)
    {
        memset(buf, 0, 20);
        while(fgets(buf, 20, fsub))
        {
            getSlidePhoto(buf, &(slides[slideIdx]));

            PHOTO *photo1 = &(photos[slides[slideIdx].photos[0]]);
            PHOTO *photo2 = NULL;

            if (-1 != slides[slideIdx].photos[1])
            {
                photo2 = &(photos[slides[slideIdx].photos[1]]);
            }
            getSlideTag(&(slides[slideIdx]), photo1, photo2);
            memset(buf, 0, 20);
            slideIdx++;
        }
    }

    if (0 != logFlag)
        printSlide(slides, slideNum);

    score = getScore(slides, slideNum);
    printf("Score: %d\n", score);

    free(photos);
    free(slides);
    fclose(fin);
    fclose(fsub);
    return 0;
}
