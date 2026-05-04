# ZDI-23-684: Delta Electronics InfraSuite Device Master ExeCommandInCommandLineMode Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-684
- **ZDI-CAN:** ZDI-CAN-19446
- **Date:** 2023-05-17
- **CVE:** CVE-2023-1141
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-684/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics InfraSuite Device Master. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the ExeCommandInCommandLineMode function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-080-02

## Disclosure Timeline

- 2022-11-10 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
