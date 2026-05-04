# ZDI-25-754: (Pwn2Own) QNAP TS-464 privWizard.cgi Authentication CRLF Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-754
- **ZDI-CAN:** ZDI-CAN-25653
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** Chris Anastasio @mufinnnnnnn & Fabius Watson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-754/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to escalate privileges on affected installations of QNAP TS-464 devices. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the privWizard.cgi endpoint. The issue results from the lack of proper neutralization of CRLF sequences. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
