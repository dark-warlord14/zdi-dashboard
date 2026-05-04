# ZDI-17-823: Apple Safari JSString Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-823
- **ZDI-CAN:** ZDI-CAN-4771
- **Date:** 2017-09-26
- **CVE:** CVE-2017-7095
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Wang Junjie Wei Lei and Liu Yang of Nanyang Technological University
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-823/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JSString objects. By performing actions in JavaScript, an attacker can trigger a memory access past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/HT208116

## Disclosure Timeline

- 2017-05-06 - Vulnerability reported to vendor
- 2017-09-26 - Coordinated public release of advisory
