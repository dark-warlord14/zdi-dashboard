# ZDI-07-039: Symantec AntiVirus Engine RAR File Parsing DoS Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-039
- **ZDI-CAN:** ZDI-CAN-097
- **Date:** 2007-07-12
- **CVE:** CVE-2007-3699
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec
- **Affected Products:** Symantec AntiVirus Engine
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-039/
## Vulnerability Details

This vulnerability allows attackers to create a denial of service condition on software with vulnerable installations of the Symantec's AntiVirus engine. Authentication is not required to exploit this vulnerability. The specific flaw resides in a forged PACK_SIZE field of a RAR file header. By setting this field to a specific value an infinite loop denial of service condition will occur when the scanner processes the file.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/avcenter/security/Content/2007.07.11f.html

## Disclosure Timeline

- 2006-11-01 - Vulnerability reported to vendor
- 2007-07-12 - Coordinated public release of advisory
