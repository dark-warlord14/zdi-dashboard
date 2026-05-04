# ZDI-24-848: (Pwn2Own) Alpine Halo9 DecodeUTF7 Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-848
- **ZDI-CAN:** ZDI-CAN-23249
- **Date:** 2024-06-21
- **CVE:** CVE-2024-23935
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Alpine
- **Affected Products:** Halo9
- **Credit:** @vudq16, @_q5ca
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-848/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Alpine Halo9 devices. An attacker must first obtain the ability to pair a malicious Bluetooth device with the target system in order to exploit this vulnerability. The specific flaw exists within the DecodeUTF7 function. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Alpine conducted a Threat Assessment and Remediation Analysis (TARA) in accordance with ISO21434, and concluded that the vulnerability is classified as "Sharing the Risk". Alpine states that they will continue to use the current software without a releasing patch.

## Disclosure Timeline

- 2024-02-01 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
