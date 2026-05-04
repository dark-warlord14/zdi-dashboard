# ZDI-16-536: Adobe Acrobat Reader DC Search Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-536
- **ZDI-CAN:** ZDI-CAN-3825
- **Date:** 2016-10-11
- **CVE:** CVE-2016-6944
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-536/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Search object. The issue lies in the failure to properly validate the existence of an object prior to performing operations on it. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-33.html

## Disclosure Timeline

- 2016-06-14 - Vulnerability reported to vendor
- 2016-10-11 - Coordinated public release of advisory
