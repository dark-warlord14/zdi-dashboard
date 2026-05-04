# ZDI-21-1593: Veritas Enterprise Vault EVStorageQueueBroker Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1593
- **ZDI-CAN:** ZDI-CAN-14079
- **Date:** 2021-12-23
- **CVE:** CVE-2021-44682
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Veritas
- **Affected Products:** Enterprise Vault
- **Credit:** Markus Wulftange (@mwulftange)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1593/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Veritas Enterprise Vault. Authentication is not required to exploit this vulnerability. The specific flaw exists within EVStorageQueueBroker.exe. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the Enterprise Vault Storage Service.

## Additional Details

Veritas has issued an update to correct this vulnerability. More details can be found at: https://www.veritas.com/content/support/en_US/security/VTS21-003

## Disclosure Timeline

- 2021-08-13 - Vulnerability reported to vendor
- 2021-12-23 - Coordinated public release of advisory
