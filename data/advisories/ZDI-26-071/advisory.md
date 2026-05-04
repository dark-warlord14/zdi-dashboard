# ZDI-26-071: Nagios Host monitoringwizard Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-071
- **ZDI-CAN:** ZDI-CAN-28245
- **Date:** 2026-02-12
- **CVE:** CVE-2026-2042
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Nagios
- **Affected Products:** Host
- **Credit:** Vladislav Berghici of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-071/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Nagios Host. Authentication is required to exploit this vulnerability. The specific flaw exists within the monitoringwizard module. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Nagios has issued an update to correct this vulnerability. More details can be found at: https://www.nagios.com/changelog/nagios-xi/nagios-xi-2026r1-0-1/

## Disclosure Timeline

- 2025-10-08 - Vulnerability reported to vendor
- 2026-02-12 - Coordinated public release of advisory
- 2026-02-12 - Advisory Updated
