# ZDI-25-646: Amazon AWS Client VPN Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-646
- **ZDI-CAN:** ZDI-CAN-26780
- **Date:** 2025-07-24
- **CVE:** CVE-2025-8069
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Amazon
- **Affected Products:** AWS Client VPN
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-646/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Amazon AWS Client VPN. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The process loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Amazon has issued an update to correct this vulnerability. More details can be found at: https://aws.amazon.com/security/security-bulletins/AWS-2025-014/

## Disclosure Timeline

- 2025-05-21 - Vulnerability reported to vendor
- 2025-07-24 - Coordinated public release of advisory
- 2025-07-24 - Advisory Updated
