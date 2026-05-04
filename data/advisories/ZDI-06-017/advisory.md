# ZDI-06-017: Microsoft Internet Explorer UTF-8 Decoding Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-017
- **ZDI-CAN:** ZDI-CAN-012
- **Date:** 2006-06-13
- **CVE:** CVE-2006-2382
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-017/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. Successful exploitation requires that the target user browse to a malicious web page. Exploitaton does not require JavaScript, Java or ActiveX to be enabled. The specific vulnerability is due to a miscalculation of memory sizes when translating UTF-8 characters to Unicode. A size mismatch between a heap allocation and memory copy results in an exploitable heap corruption.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS06-021.mspx

## Disclosure Timeline

- 2006-01-20 - Vulnerability reported to vendor
- 2006-06-13 - Coordinated public release of advisory
