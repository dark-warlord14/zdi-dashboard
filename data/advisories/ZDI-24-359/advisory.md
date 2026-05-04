# ZDI-24-359: Flexera Software FlexNet Publisher Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-359
- **ZDI-CAN:** ZDI-CAN-22591
- **Date:** 2024-04-01
- **CVE:** CVE-2024-2658
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Flexera Software
- **Affected Products:** FlexNet Publisher
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-359/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Flexera Software FlexNet Publisher. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The process loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the service account.

## Additional Details

Flexera Software has issued an update to correct this vulnerability. More details can be found at: https://community.flexera.com/t5/FlexNet-Publisher-Knowledge-Base/CVE-2024-2658-FlexNet-Publisher-potential-local-privilege/ta-p/313003

## Disclosure Timeline

- 2023-11-28 - Vulnerability reported to vendor
- 2024-04-01 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
