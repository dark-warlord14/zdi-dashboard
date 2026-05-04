# ZDI-22-015: Trend Micro Worry-Free Business Security Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-015
- **ZDI-CAN:** ZDI-CAN-14967
- **Date:** 2022-01-06
- **CVE:** CVE-2021-45442
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Worry-Free Business Security
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-015/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Trend Micro Worry-Free Business Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Trend Micro Security Agent Listener service. By creating a symbolic link, an attacker can abuse the service to overwrite a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000289996

## Disclosure Timeline

- 2021-08-18 - Vulnerability reported to vendor
- 2022-01-06 - Coordinated public release of advisory
