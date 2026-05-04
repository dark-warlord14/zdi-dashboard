# ZDI-20-977: Micro Focus Secure Messaging Gateway manage_domains_save_data SaveData Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-977
- **ZDI-CAN:** ZDI-CAN-10333
- **Date:** 2020-08-10
- **CVE:** N/A
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Micro Focus
- **Affected Products:** Secure Messaging Gateway
- **Credit:** Mehmet D. INCE @mdisec from T0.group
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-977/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Micro Focus Secure Messaging Gateway. Authentication is required to exploit this vulnerability. The specific flaw exists within manage_domains_save_data.php. When parsing the SaveData parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the www-data user.

## Additional Details

Micro Focus has issued an update to correct this vulnerability. More details can be found at: https://support.microfocus.com/kb/doc.php?id=7024775

## Disclosure Timeline

- 2020-03-03 - Vulnerability reported to vendor
- 2020-08-10 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
