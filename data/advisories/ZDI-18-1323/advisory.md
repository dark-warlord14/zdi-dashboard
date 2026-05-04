# ZDI-18-1323: Apple Safari WebCrypto Race Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1323
- **ZDI-CAN:** ZDI-CAN-6388
- **Date:** 2018-10-30
- **CVE:** CVE-2018-4373
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** ngg alippai DirtYiCE KT of Tresorit
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1323/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of WebCrypto. The issue lies in the lack of proper locking prior to executing operations in a separate thread. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2018-06-22 - Vulnerability reported to vendor
- 2018-10-30 - Coordinated public release of advisory
- 2018-10-30 - Advisory Updated
