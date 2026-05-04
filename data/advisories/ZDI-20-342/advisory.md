# ZDI-20-342: IBM Spectrum Protect Plus timezone Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-342
- **ZDI-CAN:** ZDI-CAN-9753
- **Date:** 2020-03-31
- **CVE:** CVE-2020-4206
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** IBM
- **Affected Products:** Spectrum Protect Plus
- **Credit:** Jeremy Brown
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-342/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of IBM Spectrum Protect Plus. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the Administrative Console Framework service. When parsing the timezone parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www.ibm.com/support/pages/node/6114130

## Disclosure Timeline

- 2019-12-11 - Vulnerability reported to vendor
- 2020-03-31 - Coordinated public release of advisory
