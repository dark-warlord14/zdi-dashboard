# ZDI-18-1343: Apple macOS IntelFBClientControl doAtribute Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1343
- **ZDI-CAN:** ZDI-CAN-6146
- **Date:** 2018-11-05
- **CVE:** CVE-2018-4351
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Appology Team @ Theori
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1343/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of IntelFBClientControl's doAttribute method. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT209139

## Disclosure Timeline

- 2018-06-14 - Vulnerability reported to vendor
- 2018-11-05 - Coordinated public release of advisory
- 2018-11-05 - Advisory Updated
