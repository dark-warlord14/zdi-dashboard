# ZDI-23-897: Progress Software MOVEit Transfer UserProcessPassChangeRequest SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-897
- **ZDI-CAN:** ZDI-CAN-21496
- **Date:** 2023-07-05
- **CVE:** CVE-2023-36934
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** MOVEit Transfer
- **Credit:** Guy Lederfein of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-897/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Progress Software MOVEit Transfer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the human.aspx endpoint. A crafted request can trigger execution of SQL queries composed from a user-supplied string. An attacker can leverage this vulnerability to execute code in the context of the moveitsvc user.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://community.progress.com/s/article/MOVEit-Transfer-2020-1-Service-Pack-July-2023

## Disclosure Timeline

- 2023-06-22 - Vulnerability reported to vendor
- 2023-07-05 - Coordinated public release of advisory
- 2023-07-06 - Advisory Updated
