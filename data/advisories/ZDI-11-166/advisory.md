# ZDI-11-166: HP 3COM/H3C Intelligent Management Center imcsyslogdm Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-166
- **ZDI-CAN:** ZDI-CAN-1028
- **Date:** 2011-05-10
- **CVE:** CVE-2011-1854
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** H3C Intelligent Management Center
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-166/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP 3com/H3C Intelligent Management Center. Authentication is not required to exploit this vulnerability. The flaw exists within the imcsyslogdm.exe component which listens by default on UDP port 514. When handling a syslog packet having a size larger than 2048 bytes the process attempts to exit. An exception handler is called that makes a call into a location that has been previously freed. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02822750

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-05-10 - Coordinated public release of advisory
