/* Link load transaction data from ZODAT_LINK
*/
LINK ZODAT_LINK TO :$.PAR ;
:L = :LN = :PARENT = :ATTEMPT = 0;
:LINE = :INT1 = :INT2 = :INT3 = 0 ;
:RECORDTYPE = :TEXT1 = :TEXT2 = :TEXT3 = :TEXT4 = '';
:REAL1 = 0.0
;
SELECT PARENT
INTO :PARENT
FROM ZODAT_LINK
WHERE RECORDTYPE = '1'
;
/* Fix the last attempt if the procedure failed
*/
SELECT MAX(ATTEMPT) + 1
INTO :ATTEMPT
FROM ZODAT_TRANS
WHERE LINE = :PARENT
;
SELECT SQL.TMPFILE
INTO :GEN FROM DUMMY;
LINK GENERALLOAD TO :GEN;
GOTO 500 WHERE :RETVAL <= 0
;
INSERT INTO GENERALLOAD ( RECORDTYPE , LINE )
VALUES ( '1' , 1 );
UPDATE GENERALLOAD SET TEXT1 = '10'
WHERE RECORDTYPE = '1'
;
DECLARE E2 CURSOR FOR
SELECT RECORDTYPE , LINE ,
INT1 , INT2 , INT3 ,
TEXT1 , TEXT2 , TEXT3 , TEXT4 , TEXT5 ,
REAL1
FROM ZODAT_LINK
WHERE 0=0
AND LINE > 0
AND LOADED = ''
;
OPEN E2;
GOTO 9 WHERE :RETVAL = 0;
LABEL 1;
FETCH E2 INTO :RECORDTYPE , :LINE ,
:INT1 , :INT2 , :INT3 ,
:TEXT1 , :TEXT2 , :TEXT3 , :TEXT4 , :TEXT5 ,
:REAL1 ;
GOTO 8 WHERE :RETVAL = 0;
/*
*/
GOSUB 100 WHERE :RECORDTYPE = '1';
GOSUB 200 WHERE :RECORDTYPE = '2';
GOSUB 300 WHERE :RECORDTYPE = '3';
GOSUB 400 WHERE :RECORDTYPE = '4';
GOSUB 500 WHERE :RECORDTYPE = '5';
GOSUB 600 WHERE :RECORDTYPE = '6';
GOSUB 700 WHERE :RECORDTYPE = '7';
GOSUB 800 WHERE :RECORDTYPE = '8';
GOSUB 900 WHERE :RECORDTYPE = '9';
LOOP 1;
LABEL 8;
CLOSE E2;
LABEL 9;
SELECT * FROM GENERALLOAD
WHERE LINE > 0
FORMAT ADDTO '../../GENLOAD.TXT'
;
/* Run Interface*/
EXECUTE INTERFACE 'ZOBNK_LOADTRANS', SQL.TMPFILE, '-L', :GEN
;
INSERT INTO ZODAT_ERR
(ATTEMPT , LOGTIME , LINE , PARENT , MESSAGE)
SELECT :ATTEMPT , SQL.DATE, LINE, :PARENT, MESSAGE
FROM ERRMSGS
WHERE 0=0
AND TYPE ='i'
AND USER = SQL.USER
;
SELECT :ATTEMPT , SQL.DATE, LINE, :PARENT, MESSAGE
FROM ERRMSGS
WHERE 0=0
AND TYPE ='i'
AND USER = SQL.USER
FORMAT '../../ATTEMPT.TXT'
;
UPDATE ZODAT_LINK
SET LOADED = 'L'
WHERE LINE = :LN
AND NOT EXISTS(
SELECT * FROM ZODAT_ERR
WHERE 0=0
AND ATTEMPT = :ATTEMPT
AND LINE = :LN
AND PARENT = :PARENT
);
UNLINK GENERALLOAD ;
LABEL 500;
END;
/* */
SUB 100;
SELECT 1 + MAX(LINE)
INTO :L
FROM GENERALLOAD;
INSERT INTO GENERALLOAD(RECORDTYPE , LINE)
VALUES
('2' , :L);
UPDATE GENERALLOAD SET
TEXT1 = :TEXT1 ,
TEXT2 = :TEXT2 ,
TEXT3 = :TEXT3 ,
TEXT4 = :TEXT4 ,
TEXT5 = :TEXT5 ,
INT1 = :INT1 ,
INT2 = :INT2 ,
INT3 = :INT3 ,
REAL1 = :REAL1,
TEXT18 = '00'
WHERE LINE = :L;
RETURN;
SUB 200;
UPDATE GENERALLOAD SET
REAL2 = REAL1,
TEXT6 = TEXT1
WHERE LINE = :L;
RETURN;
SUB 300;
UPDATE GENERALLOAD SET
TEXT7 = TEXT1 ,
TEXT8 = TEXT2
WHERE LINE = :L;
RETURN;
SUB 400;
UPDATE GENERALLOAD SET
TEXT9 = TEXT1 ,
TEXT10 = TEXT2
WHERE LINE = :L;
RETURN;
SUB 500;
UPDATE GENERALLOAD SET
TEXT11 = TEXT1 ,
TEXT12 = TEXT2
WHERE LINE = :L;
RETURN;
SUB 600;
UPDATE GENERALLOAD SET
TEXT13 = TEXT1 ,
TEXT14 = TEXT2
WHERE LINE = :L;
RETURN;
SUB 700;
UPDATE GENERALLOAD SET
TEXT15 = TEXT1
WHERE LINE = :L;
RETURN;
SUB 800;
UPDATE GENERALLOAD SET
REAL3 = REAL1 ,
TEXT16 = TEXT1
WHERE LINE = :L;
RETURN;
SUB 900;
UPDATE GENERALLOAD SET
TEXT17 = TEXT1
WHERE LINE = :L;
RETURN;
