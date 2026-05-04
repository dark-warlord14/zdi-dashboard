# ZDI-07-034: CA Multiple Product AV Engine CAB Filename Parsing Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-034
- **ZDI-CAN:** ZDI-CAN-123
- **Date:** 2007-06-05
- **CVE:** CVE-2007-2863
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Computer Associates
- **Affected Products:** eTrust AntiVirus
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-034/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of various Computer Associates products. The specific flaw exists in the parsing of .CAB archives. When a long filename contained in the .CAB is processed by vete.dll an exploitable stack overflow may occur.

## Additional Details

Computer Associates has issued an update to correct this vulnerability. More details can be found at: http://supportconnectw.ca.com/public/antivirus/infodocs/caantivirus-securitynotice.asp

## Disclosure Timeline

- 2006-11-08 - Vulnerability reported to vendor
- 2007-06-05 - Coordinated public release of advisory
