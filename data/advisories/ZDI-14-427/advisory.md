# ZDI-14-427: Mozilla Firefox DirectionalityUtils Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-427
- **ZDI-CAN:** ZDI-CAN-2531
- **Date:** 2015-02-23
- **CVE:** CVE-2014-1581
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-427/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of bi-directional unicode text. The issue lies in the failure to properly handle text that has its bi-directional character type changed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2014-79/

## Disclosure Timeline

- 2014-09-16 - Vulnerability reported to vendor
- 2015-02-23 - Coordinated public release of advisory
