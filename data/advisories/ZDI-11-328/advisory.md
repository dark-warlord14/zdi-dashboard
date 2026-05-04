# ZDI-11-328: ProFTPD Response Pool Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-328
- **ZDI-CAN:** ZDI-CAN-1420
- **Date:** 2011-11-11
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** ProFTPD
- **Affected Products:** FTP Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-328/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the ProFTPd server. Authentication is required to exploit this vulnerability in order to have access to the ftp command set. The specific flaw exists within how the server manages the response pool that is used to send responses from the server to the client. When handling an exceptional condition the application will fail to restore the original response pointer which will allow there to be more than one reference to the response pointer. The next time it is used, a memory corruption can be made to occur which can allow for code execution under the context of the application.

## Additional Details

ProFTPD has issued an update to correct this vulnerability. More details can be found at: http://bugs.proftpd.org/show_bug.cgi?id=3711

## Disclosure Timeline

- 2011-10-28 - Vulnerability reported to vendor
- 2011-11-11 - Coordinated public release of advisory
