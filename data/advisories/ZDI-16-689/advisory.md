# ZDI-16-689: Microsoft Internet Explorer Array.splice Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-689
- **ZDI-CAN:** ZDI-CAN-4319
- **Date:** 2017-06-21
- **CVE:** CVE-2016-7202
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Li Kemeng of Baidu Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-689/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the JavaScript method Array.splice. By performing actions in JavaScript an attacker can corrupt the state of a JavaScript array. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/ms16-144

## Disclosure Timeline

- 2016-12-12 - Vulnerability reported to vendor
- 2017-06-21 - Coordinated public release of advisory
