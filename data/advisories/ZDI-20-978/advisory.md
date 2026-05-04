# ZDI-20-978: Canonical Ubuntu apport Unnecessary Privileges Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-978
- **ZDI-CAN:** ZDI-CAN-11233
- **Date:** 2020-08-11
- **CVE:** CVE-2020-11936
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Canonical
- **Affected Products:** Ubuntu
- **Credit:** Ryota Shiga(@Ga_ryo_) of Flatt Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-978/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Canonical Ubuntu. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the apport package. The issue results from the use of unnecessary privileges. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of root.

## Additional Details

Canonical has issued an update to correct this vulnerability. More details can be found at: https://ubuntu.com/security/notices/USN-4449-1

## Disclosure Timeline

- 2020-06-26 - Vulnerability reported to vendor
- 2020-08-11 - Coordinated public release of advisory
