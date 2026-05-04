# ZDI-15-438: Cogent DataHub Gamma Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-438
- **ZDI-CAN:** ZDI-CAN-2981
- **Date:** 2015-09-08
- **CVE:** CVE-2014-3789
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cogent Real-Time Systems
- **Affected Products:** Cogent Datahub
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-438/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cogent DataHub. Authentication is not required to exploit this vulnerability. The specific flaw exists within the EvalExpresssion method, which is available remotely through the AJAX facility. Using this method, it is possible to execute arbitrary Gamma code. By supplying a specially formatted Gamma script, a remote attacker can execute arbitrary OS commands in the context of the DataHub process.

## Additional Details

Cogent Real-Time Systems has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-246-01

## Disclosure Timeline

- 2015-06-02 - Vulnerability reported to vendor
- 2015-09-08 - Coordinated public release of advisory
