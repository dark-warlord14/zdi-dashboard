# ZDI-16-591: Adobe Reader DC XObject stream Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-591
- **ZDI-CAN:** ZDI-CAN-3842
- **Date:** 2016-11-04
- **CVE:** CVE-2016-6938
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-591/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of XObject streams. The issue lies in the failure to properly validate the existence of an object prior to performing operations on it. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-26.html

## Disclosure Timeline

- 2016-06-28 - Vulnerability reported to vendor
- 2016-11-04 - Coordinated public release of advisory
