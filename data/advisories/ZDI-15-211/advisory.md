# ZDI-15-211: Adobe Acrobat Pro Spell customDictionaryExport Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-211
- **ZDI-CAN:** ZDI-CAN-2706
- **Date:** 2015-05-12
- **CVE:** CVE-2015-3058
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-211/
## Vulnerability Details

This vulnerability allows remote attackers to leak memory addresses from Spell.api on vulnerable installations of Adobe Acrobat Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Spell object. By creating and exporting a custom dictionary, it is possible to leak memory addresses from Spell.api. An attacker can leverage this vulnerability to disclose arbitrary memory.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-10.html

## Disclosure Timeline

- 2015-01-27 - Vulnerability reported to vendor
- 2015-05-12 - Coordinated public release of advisory
