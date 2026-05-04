# ZDI-11-116: Novell File Reporter Agent XML Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-116
- **ZDI-CAN:** ZDI-CAN-830
- **Date:** 2011-04-04
- **CVE:** CVE-2011-0994
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** File Reporter
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-116/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell File Reporter Agent. Authentication is not required to exploit this vulnerability. The flaw exists within the NFRAgent.exe component which listens by default on TCP port 3037. When handling the contents of an XML tag the process blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=rCAgCcbPH9s~

## Disclosure Timeline

- 2010-10-06 - Vulnerability reported to vendor
- 2011-04-04 - Coordinated public release of advisory
