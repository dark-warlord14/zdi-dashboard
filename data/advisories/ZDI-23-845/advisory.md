# ZDI-23-845: (Pwn2Own) Apple macOS /dev/fd Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-845
- **ZDI-CAN:** ZDI-CAN-20714
- **Date:** 2023-06-08
- **CVE:** CVE-2023-32413
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Eloi Benoist-Vanderbeken (@elvanderb) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-845/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the /dev/fd filesystem. The issue results from the lack of proper locking when performing operations on a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT213758

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
