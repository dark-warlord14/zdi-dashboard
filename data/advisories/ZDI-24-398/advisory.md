# ZDI-24-398: Wazuh Active Response Module Improper Input Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-398
- **ZDI-CAN:** ZDI-CAN-22560
- **Date:** 2024-04-25
- **CVE:** CVE-2023-50260
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Wazuh
- **Affected Products:** Wazuh
- **Credit:** @d0ntrash
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-398/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Wazuh. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of IP address arguments. The issue results from the lack of proper validation of JSON messages. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Wazuh has issued an update to correct this vulnerability. More details can be found at: https://github.com/wazuh/wazuh/security/advisories/GHSA-mjq2-xf8g-68vw

## Disclosure Timeline

- 2023-11-28 - Vulnerability reported to vendor
- 2024-04-25 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
