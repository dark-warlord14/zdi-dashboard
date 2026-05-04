# ZDI-18-877: TripAdvisor Browsable Intent Arbitrary URL Loading Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-877
- **ZDI-CAN:** ZDI-CAN-5335
- **Date:** 2018-08-02
- **CVE:** CVE-2017-17226
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** TripAdvisor
- **Affected Products:** TripAdvisor
- **Credit:** Tencent Keen Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-877/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of TripAdvisor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of browsable intents. The issue results from improper validation on user-supplied URLs. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the application.

## Additional Details

TripAdvisor has issued an update to correct this vulnerability. More details can be found at: http://www.huawei.com/en/psirt/security-advisories/huawei-sa-20180130-01-tripadvisor-en

## Disclosure Timeline

- 2017-11-01 - Vulnerability reported to vendor
- 2018-08-02 - Coordinated public release of advisory
- 2018-08-02 - Advisory Updated
