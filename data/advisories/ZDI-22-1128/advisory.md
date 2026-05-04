# ZDI-22-1128: AVEVA Edge LoadImportedLibraries XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1128
- **ZDI-CAN:** ZDI-CAN-17394
- **Date:** 2022-08-23
- **CVE:** CVE-2022-36969
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** AVEVA
- **Affected Products:** Edge
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1128/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of AVEVA Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the LoadImportedLibraries method. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

AVEVA has issued an update to correct this vulnerability. More details can be found at: https://www.aveva.com/content/dam/aveva/documents/support/cyber-security-updates/SecurityBulletin_AVEVA-2022-005.pdf

## Disclosure Timeline

- 2022-05-17 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
