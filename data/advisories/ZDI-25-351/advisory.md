# ZDI-25-351: Pioneer DMH-WT7600NEX Missing Immutable Root of Trust in Hardware Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-351
- **ZDI-CAN:** ZDI-CAN-26078
- **Date:** 2025-06-11
- **CVE:** CVE-2025-5834
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Pioneer
- **Affected Products:** DMH-WT7600NEX
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-351/
## Vulnerability Details

This vulnerability allows local attackers to bypass authentication on affected installations of Pioneer DMH-WT7600NEX devices. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the configuration of the application system-on-chip (SoC). The issue results from the lack of a properly configured hardware root of trust. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the boot process.

## Additional Details

Fixed in Version 3.07 https://www.pioneerelectronics.com/PUSA/Support/Downloads

## Disclosure Timeline

- 2025-01-14 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-08-28 - Advisory Updated
