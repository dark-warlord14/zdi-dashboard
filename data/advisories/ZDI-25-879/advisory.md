# ZDI-25-879: Realtek rtl81xx SDK Wi-Fi Driver rtwlanu Heap-based Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-879
- **ZDI-CAN:** ZDI-CAN-26553
- **Date:** 2025-09-02
- **CVE:** CVE-2025-8302
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Realtek
- **Affected Products:** rtl81xx SDK
- **Credit:** dungnm from vcslab of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-879/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Realtek rtl81xx SDK Wi-Fi driver. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the N6CSet_DOT11_CIPHER_DEFAULT_KEY function. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in v1030.44.1204.2024 - https://www.realtek.com/Article/Index?menu_id=848

## Disclosure Timeline

- 2025-02-21 - Vulnerability reported to vendor
- 2025-09-02 - Coordinated public release of advisory
- 2025-09-02 - Advisory Updated
