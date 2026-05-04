# ZDI-11-209: Adobe Shockwave rcsL Substructure Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-209
- **ZDI-CAN:** ZDI-CAN-1216
- **Date:** 2011-06-14
- **CVE:** CVE-2011-0335
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-209/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the rcsL chunk inside Adobe's RIFF-based Director file format. The code within the Dirapi.dll is affected by an integer wrap caused by the size value being calculated from the difference of two pointers without checking if the first is above the other and resulting in endless copying. This can lead to memory corruption which can be leveraged to execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-04-20 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
