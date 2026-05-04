# ZDI-11-350: Enterasys NetSight nssyslogd PRI Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-350
- **ZDI-CAN:** ZDI-CAN-1099
- **Date:** 2011-12-19
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Enterasys
- **Affected Products:** NetSight
- **Credit:** Jeremy Brown Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-350/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Enterasys Netsight. Authentication is not required to exploit this vulnerability. The flaw exists within the nssyslogd.exe component which listens by default on UDP port 514. When parsing a new syslog message the process attempts to copy the PRIO field to an intermediate variable. The process does not properly validate the size of the destination buffer and blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Enterasys has issued an update to correct this vulnerability. More details can be found at: https://cp-enterasys.kb.net/article.aspx?article=14206&p=1

## Disclosure Timeline

- 2011-04-27 - Vulnerability reported to vendor
- 2011-12-19 - Coordinated public release of advisory
