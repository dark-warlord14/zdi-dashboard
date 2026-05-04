# ZDI-24-397: Wazuh Analysis Engine Event Decoder Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-397
- **ZDI-CAN:** ZDI-CAN-22475
- **Date:** 2024-04-25
- **CVE:** CVE-2024-32038
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Wazuh
- **Affected Products:** Wazuh
- **Credit:** @d0ntrash
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-397/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Wazuh. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Analysis Engine service, which listens on TCP port 1514 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Wazuh has issued an update to correct this vulnerability. More details can be found at: https://github.com/wazuh/wazuh/security/advisories/GHSA-fcpw-v3pg-c327

## Disclosure Timeline

- 2023-11-28 - Vulnerability reported to vendor
- 2024-04-25 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
