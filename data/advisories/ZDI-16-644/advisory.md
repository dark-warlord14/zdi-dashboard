# ZDI-16-644: Apple OS X AppleBroadcomBluetoothHostController Type Confusion Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-644
- **ZDI-CAN:** ZDI-CAN-4019
- **Date:** 2016-12-15
- **CVE:** CVE-2016-7617
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Radu Motspan
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-644/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the AppleBroadcomBluetoothHostController kext. The issue results from the lack of proper validation of user-supplied data which can result in a type confusion condition. An attacker can leverage this vulnerability to escalate privileges under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207423

## Disclosure Timeline

- 2016-09-08 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
