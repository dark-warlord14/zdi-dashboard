# ZDI-24-182: ESET Smart Security Premium ekrn Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-182
- **ZDI-CAN:** ZDI-CAN-22323
- **Date:** 2024-02-15
- **CVE:** CVE-2024-0353
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ESET
- **Affected Products:** Smart Security Premium
- **Credit:** Nicholas Zubrisky and Michael DePlante (@izobashi) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-182/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of ESET Smart Security Premium. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ESET Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

ESET has issued an update to correct this vulnerability. More details can be found at: https://support.eset.com/en/ca8612-eset-customer-advisory-link-following-local-privilege-escalation-vulnerability-in-eset-products-for-windows-fixed.

## Disclosure Timeline

- 2023-10-17 - Vulnerability reported to vendor
- 2024-02-15 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
