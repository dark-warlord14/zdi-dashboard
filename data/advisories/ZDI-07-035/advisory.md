# ZDI-07-035: CA Multiple Product AV Engine CAB Header Parsing Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-035
- **ZDI-CAN:** ZDI-CAN-154
- **Date:** 2007-06-05
- **CVE:** CVE-2007-2864
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Computer Associates
- **Affected Products:** eTrust AntiVirus
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-035/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of various Computer Associates products. The specific flaw exists within the processing of an improperly defined "coffFiles" field in .CAB archives. Large values result in an unbounded data copy operation which can result in an exploitable stack-based buffer overflow.

## Additional Details

Computer Associates has issued an update to correct this vulnerability. More details can be found at: http://supportconnectw.ca.com/public/antivirus/infodocs/caantivirus-securitynotice.asp

## Disclosure Timeline

- 2007-02-16 - Vulnerability reported to vendor
- 2007-06-05 - Coordinated public release of advisory
