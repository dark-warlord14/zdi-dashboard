# ZDI-06-028: Ipswitch Collaboration Suite SMTP Server Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-028
- **ZDI-CAN:** ZDI-CAN-067
- **Date:** 2006-09-08
- **CVE:** CVE-2006-4379
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Ipswitch
- **Affected Products:** IMail
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-028/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Ipswitch Collaboration Suite and IMail. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SMTP daemon. A lack of bounds checking during the parsing of long strings contained within the characters '@' and ':' leads to a stack overflow vulnerability. Exploitation can result in code execution or a denial of service.

## Additional Details

Ipswitch has issued an update to correct this vulnerability. More details can be found at: http://www.ipswitch.com/support/imail/releases/im20061.asp

## Disclosure Timeline

- 2006-06-22 - Vulnerability reported to vendor
- 2006-09-08 - Coordinated public release of advisory
