# ZDI-24-097: Wazuh Log Collector Integer Underflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-097
- **ZDI-CAN:** ZDI-CAN-22015
- **Date:** 2024-02-08
- **CVE:** CVE-2023-42463
- **CVSS:** 7.4
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Wazuh
- **Affected Products:** Wazuh
- **Credit:** Keith Yeo (@kyeojy)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-097/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Wazuh. Log Injection is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the processing of the multilines log format. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Wazuh has issued an update to correct this vulnerability. More details can be found at: https://documentation.wazuh.com/current/release-notes/release-4-5-3.html

## Disclosure Timeline

- 2023-09-14 - Vulnerability reported to vendor
- 2024-02-08 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
