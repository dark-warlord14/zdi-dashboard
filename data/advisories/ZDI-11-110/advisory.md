# ZDI-11-110: (0Day) IBM Lotus Domino Server Controller Authentication Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-110
- **ZDI-CAN:** ZDI-CAN-927
- **Date:** 2011-03-22
- **CVE:** CVE-2011-0920
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** Patrik Karlsson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-110/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Lotus Domino Server Controller. Authentication is not required to exploit this vulnerability. The flaw exists within the remote console functionality which listens by default on TCP port 2050. When handling A user authentication the server uses a user supplied COOKIEFILE path to retrieve stored credentials. The application then compares this data against the user provided username and cookie. The path to the COOKIEFILE can be a UNC path allowing the attacker to control both the known good credentials and the challenge credentials. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

March 22, 2011 - This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. -- Mitigations: Setting a console password provides another level of authentication and limits the commands available in the console. To further mitigate this vulnerability access to 2050/tcp on hosts running the Domino Server Controller application should be restricted to authorized hosts. -- February 3, 2012: IBM provided a link to their patch reference: http://www-01.ibm.com/support/docview.wss?uid=swg21461514

## Disclosure Timeline

- 2010-09-23 - Vulnerability reported to vendor
- 2011-03-22 - Coordinated public release of advisory
