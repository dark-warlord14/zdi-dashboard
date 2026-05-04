# ZDI-21-900: Adobe After Effects PDF File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-900
- **ZDI-CAN:** ZDI-CAN-13859
- **Date:** 2021-07-28
- **CVE:** CVE-2021-36017
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** After Effects
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-900/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe After Effects. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/after_effects/apsb21-54.html

## Disclosure Timeline

- 2021-06-02 - Vulnerability reported to vendor
- 2021-07-28 - Coordinated public release of advisory
