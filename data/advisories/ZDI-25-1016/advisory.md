# ZDI-25-1016: Wibu-Systems WibuKey Runtime Untrusted Pointer Dereference Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1016
- **ZDI-CAN:** ZDI-CAN-27540
- **Date:** 2025-11-25
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Wibu-Systems
- **Affected Products:** WibuKey
- **Credit:** 김명규
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1016/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Wibu-Systems WibuKey Runtime. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Wibukey2_64.sys driver. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Wibu-Systems has issued an update to correct this vulnerability. More details can be found at: https://cdn.wibu.com/fileadmin/wibu_downloads/security_advisories/AdvisoryWIBU-100031.pdf

## Disclosure Timeline

- 2025-07-22 - Vulnerability reported to vendor
- 2025-11-25 - Coordinated public release of advisory
- 2025-11-25 - Advisory Updated
