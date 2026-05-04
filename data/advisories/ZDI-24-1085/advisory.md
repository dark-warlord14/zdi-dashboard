# ZDI-24-1085: (0Day) oFono SimToolKit Heap-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1085
- **ZDI-CAN:** ZDI-CAN-23458
- **Date:** 2024-08-05
- **CVE:** CVE-2024-7545
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** oFono
- **Affected Products:** oFono
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1085/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of oFono. An attacker must first obtain the ability to execute code on the target modem in order to exploit this vulnerability. The specific flaw exists within the parsing of STK command PDUs. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

08/05/24 – ZDI made multiple attempts to report the vulnerability to the vendor via the oFono distribution list, Red Hat, and upstream Linux Kernel, but the vendor did not respond. The Linux Kernel informed ZDI that since it “has nothing to do with the Linux Kernel,” we should report it to the distribution list. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-02-29 - Vulnerability reported to vendor
- 2024-08-05 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
