# ZDI-25-880: Realtek RTL8811AU rtwlanu.sys N6CSet_DOT11_CIPHER_DEFAULT_KEY Heap-based Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-880
- **ZDI-CAN:** ZDI-CAN-24786
- **Date:** 2025-09-02
- **CVE:** CVE-2025-8301
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Realtek
- **Affected Products:** RTL8811AU
- **Credit:** dungnm from vcslab of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-880/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Realtek RTL8811AU drivers. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the N6CSet_DOT11_CIPHER_DEFAULT_KEY function. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in v1030.44.1204.2024 - https://www.realtek.com/Article/Index?menu_id=848

## Disclosure Timeline

- 2024-11-19 - Vulnerability reported to vendor
- 2025-09-02 - Coordinated public release of advisory
- 2025-09-02 - Advisory Updated
