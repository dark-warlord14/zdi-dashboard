# ZDI-18-1365: Apple macOS shm Uninitialized Data Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1365
- **ZDI-CAN:** ZDI-CAN-7299
- **Date:** 2018-12-10
- **CVE:** CVE-2018-4435
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Juwei Lin(@panicaII) and Junzhi Lu of TrendMicro Mobile Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1365/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the shared memory module (shm). The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT209341

## Disclosure Timeline

- 2018-09-25 - Vulnerability reported to vendor
- 2018-12-10 - Coordinated public release of advisory
