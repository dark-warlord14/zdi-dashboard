# ZDI-23-011: Microsoft Exchange TorusUpdateInitialSessionState Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-011
- **ZDI-CAN:** ZDI-CAN-19492
- **Date:** 2023-01-18
- **CVE:** CVE-2023-21763
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-011/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Exchange. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the TorusUpdateInitialSessionState function. The function loads a library from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21763

## Disclosure Timeline

- 2022-11-11 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
