# ZDI-25-881: Realtek RTL8811AU rtwlanu.sys N6CQueryInformationHandleCustomized11nOids Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-881
- **ZDI-CAN:** ZDI-CAN-25864
- **Date:** 2025-09-02
- **CVE:** CVE-2025-8298
- **CVSS:** 3.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Realtek
- **Affected Products:** RTL8811AU
- **Credit:** dungnm from vcslab of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-881/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Realtek RTL8811AU drivers. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the N6CQueryInformationHandleCustomized11nOids function. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Fixed in v1030.44.1204.2024 - https://www.realtek.com/Article/Index?menu_id=848

## Disclosure Timeline

- 2024-11-21 - Vulnerability reported to vendor
- 2025-09-02 - Coordinated public release of advisory
- 2025-09-02 - Advisory Updated
