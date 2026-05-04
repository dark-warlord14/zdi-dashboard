# ZDI-24-898: ESET Smart Security Premium Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-898
- **ZDI-CAN:** ZDI-CAN-23314
- **Date:** 2024-07-05
- **CVE:** CVE-2024-2003
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** ESET
- **Affected Products:** Smart Security Premium
- **Credit:** Nicholas Zubrisky (@NZubrisky) and Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-898/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of ESET Smart Security Premium. User interaction on the part of an administrator is required to exploit this vulnerability. The specific flaw exists within the ESET Service. By creating a symbolic link, an attacker can abuse the service to create a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

ESET has issued an update to correct this vulnerability. More details can be found at: https://support.eset.com/ca8674

## Disclosure Timeline

- 2024-02-21 - Vulnerability reported to vendor
- 2024-07-05 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
